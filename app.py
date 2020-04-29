@app.route('/checkout')
def checkout():
  intent = \Stripe\Stripe::setApiKey('sk_test_PLiOcIjAm21cud2PbXj9dK9m00PlmPubfg');

$payment_intent = \Stripe\PaymentIntent::create([
  'payment_method_types' => ['fpx'],
  'amount' => 100,
  'currency' => 'myr',
]);
  return render_template('checkout.html', client_secret=intent.client_secret)
