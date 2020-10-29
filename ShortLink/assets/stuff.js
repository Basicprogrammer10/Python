function makeid(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@$%';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;}
  function setup(){
    input = document.getElementById('login').elements[0].value;
    if (input.includes("https://")){
        console.log('Yep')
    }else if (input.includes("https://")){
        console.log('Yep')
    }else {
        console.log('Nope')
    }
    fetch(window.location+"/api/?url=""?code="+makeid(10))
    .then(function (response) {
        console.log(response)
        return response
    })
  }