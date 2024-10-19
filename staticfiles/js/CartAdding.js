function HandleAdding(product_id, quantity) {
    const csrftoken = getCookie('csrftoken');
    console.log("CSRF Token: ", csrftoken);

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

document.addEventListener("DOMContentLoaded", function() {
    console.log('Document loaded');
})