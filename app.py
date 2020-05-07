@app.route('/checkout')
def checkout():
  intent = \Stripe\Stripe::setApiKey('pk_live_y0w739w1dR6yZv3P8dfhFBCh00lEbc72UX');

$payment_intent = \Stripe\PaymentIntent::create([
  'payment_method_types' => ['fpx']['card'],
  'amount' => 10000,
  'currency' => 'myr',
]);
  return render_template('checkout.html', client_secret=intent.client_secret)
