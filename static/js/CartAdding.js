function HandleAdding(product_id, quantity) {
    const csrf_token = getCookie('csrf_token');
    console.log("test")

    fetch("{% url 'add_to_cart_ajax' %}", {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-CSRFToken': csrf_token
        },
        body: JSON.stringify({
            'product_id': product_id,
            'quantity': quantity
        })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("product added");
            } else {
                alert('Failed to add product to cart.');
            }
        })
        .catch((error) => console.error('Error:', error));
}