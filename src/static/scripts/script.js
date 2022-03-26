function getData() {
    console.log($('#state-field').val());
    console.log($('#days-field').val());
    let form = {
        state: $('state-field').val(),
        days: $('#days-field').val()
    }
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/api",
        data: form
    }).done( function(data) {
        console.log(data);
        $("main").append(`<p id="result">${data.cases}</p>`);
    });
}
