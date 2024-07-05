$ curl -X POST http://my_textbelt_server/text \
   -d number=5551234567 \
   -d "message=I sent this message for free with Textbelt"

   var text = require('textbelt');

text.send('9491234567', 'A sample text message!', undefined, function(err) {
  if (err) {
    console.log(err);
  }
});