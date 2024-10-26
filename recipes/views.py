from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import random
import json
import re
import os
from dotenv import load_dotenv
load_dotenv()


# Create your views here.
def land(request):
    return render(request, 'landingPage.html')


def getresponse(request):
    if len(request.GET) != 0:
        ingredient=request.GET.get("ingredient")
        meal_type=request.GET.get("meal_type")
        equipment=request.GET.getlist("equipment")
        time=request.GET.get('time')
        prompt = f"Ingredients: {ingredient}, Meal: {meal_type}, Time: {time}, equipment: {equipment}"
        if prompt is not None and len(prompt)>0: #Check whether the length of string is not zero and not None
            api_key = os.getenv('API_KEY')
            external_user_id = random.choice(api_key)

            # Create Chat Session
            create_session_url = 'https://api.on-demand.io/chat/v1/sessions'
            create_session_headers = {
                'apikey': api_key
            }
            create_session_body = {
                "pluginIds": [],
                "externalUserId": external_user_id
            }

            # Make the request to create a chat session
            response = requests.post(create_session_url, headers=create_session_headers, json=create_session_body)
            response_data = response.json()

            # Extract session ID from the response
            session_id = response_data['data']['id']

            # Submit Query
            submit_query_url = f'https://api.on-demand.io/chat/v1/sessions/{session_id}/query'
            submit_query_headers = {
                'apikey': api_key
            }
            submit_query_body = {
                "endpointId": "predefined-openai-gpt4o",
                "query": prompt,
                "pluginIds": ["plugin-1712327325", "plugin-1713962163"],
                "responseMode": "sync",
                "modelConfigs": {
                    "fulfillmentPrompt": "Provide Indian style three recipes using only the listed ingredients, assuming basic Indian spices (such as mustard seeds, turmeric, cumin, chili powder, and salt) and using the cookware mentioned with cuisine type and time to make it.\nPlease provide the recipe information in JSON format with fields of name, preparation_time(with unit), macros(with unit)(calories, protein, carbohydrates, fats), ingredients and instructions.\nMake sure each field matches this structure.\nQuestion: {question}\nContext: {context}"
                }
            }
            


            # Make the request to submit a query
            query_response = requests.post(submit_query_url, headers=submit_query_headers, json=submit_query_body)
            query_response_data = query_response.json()
            try:
                answer_text = query_response_data['data']['answer']

            except:
                return render(request, "notFound.html")
            json_str = re.sub(r'```json|```', '', answer_text).strip()
     

            try:
                recipes = json.loads(json_str)
            except:
                return render(request, "notFound.html")


            print(recipes)
            return render(request, "result.html", {
                'recipes':recipes
            })

            # try:
            #     return render(request, "result.html", {
            #         'recipes':recipes
            #     })
            # except:
            #     render(request, "notFound.html")
    return render(request, 'getPrompt.html')

def about(request):
    return render(request, 'about.html')
