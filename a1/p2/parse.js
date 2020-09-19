let sig_data = {};

$('.wikitable tr').each(function() {
    let offset = $(this).find($(this).children()[2]).html();
    let cell0 = $(this).find($(this).children()[0]);
    let type = $(this).find($(this).children()[3]).html();
    cell0.find($('pre')).each( function() {
        sig_data[$(this).html()] = {
            signature: $(this).html(),
            offset: offset.split('<p>any</p>').join(''),
            type: type
        }
    } );
});

console.log(JSON.stringify(sig_data));