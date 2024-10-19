function HandleAdding(product_id, quantity) {
    const csrftoken = getCookie('csrftoken');
    console.log("CSRF Token: ", csrftoken);
    console.log("id:", product_id, "quantity:", quantity);

    fetch(addToCartUrl, {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            'product_id': product_id,
            'quantity': quantity
        })
    })
        .then(response => response.json())  // Ожидаем JSON в ответе
        .then(data => {
            console.log('Response from server:', data);  // Логируем ответ
            if (data.success) {
                alert("Product added");
            } else {
                alert('Failed to add product to cart: ' + data.error);  // Логируем ошибку
            }
        })
        .catch((error) => console.error('Error:', error));
}

document.addEventListener("DOMContentLoaded", function() {
    console.log('Document loaded');
})