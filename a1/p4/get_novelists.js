let names = {};

$('.wikitable tr').each(function() {
    let cell0 = $(this).find($(this).children()[0]);
    cell0.find($('a')).each( function() {
        let name = $(this).html();
        let url = window.location.host + $(this).attr('href');
        names[name] = url;
    } );
});

console.log(JSON.stringify(names));