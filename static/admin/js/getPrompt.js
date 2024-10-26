function addIngredient(event) {
    const input = document.getElementById('ingredientInput');
    const container = document.getElementById('ingredientsContainer');

    // Check if Enter key is pressed
    if (event.key === 'Enter' && input.value.trim() !== '') {
        const ingredientName = input.value.trim();
        const ingredientDiv = document.createElement('div');
        ingredientDiv.className = 'ingredient';
        ingredientDiv.innerHTML = `${ingredientName} <span class="remove" onclick="removeIngredient(this)">✕</span>`;
        container.appendChild(ingredientDiv);
        input.value = ''; // Clear the input
    }
}

function removeIngredient(element) {
    const ingredientDiv = element.parentElement;
    ingredientDiv.remove(); // Remove the ingredient
}