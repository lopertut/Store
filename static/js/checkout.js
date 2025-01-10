document.addEventListener('DOMContentLoaded', function() {
    const stripe = Stripe('pk_test_51QSlaeKoWxR0NlMuhSXOFjtQcgbmbtgBtwZMRqmayF8mrnyK8yhJPICMrh1y7vfYWTHuyZLSnbkr7WaYwsuTn3gH004IP4OON7');

    // Проверяем, существует ли кнопка с ID
    let checkoutButton = document.getElementById('checkout-button');
    if (checkoutButton) {
        checkoutButton.addEventListener('click', function() {
            fetch('/create-checkout-session/')
                .then(response => response.json())
                .then(data => stripe.redirectToCheckout({ sessionId: data.session_id }));
        });
    }
});
