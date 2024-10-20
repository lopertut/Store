function updateCartDisplay(productId, quantityChange) {
    let itemElement = document.getElementById(`cart-item-${productId}`);
    let quantityElement = itemElement.querySelector('.item-quantity');
    let totalPriceElement = document.getElementById('total-price');

    let currentQuantity = parseInt(quantityElement.innerText);
    let newQuantity = currentQuantity + quantityChange;

    if (newQuantity <= 0) {
        itemElement.remove();
    } else {
        quantityElement.innerText = newQuantity;
    }

    let itemPrice = parseFloat(itemElement.querySelector('.item-price').innerText);
    let currentTotalPrice = parseFloat(totalPriceElement.innerText);
    let newTotalPrice = currentTotalPrice + (itemPrice * quantityChange);

    totalPriceElement.innerText = newTotalPrice.toFixed(2);
}