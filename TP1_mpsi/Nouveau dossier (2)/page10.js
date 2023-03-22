function submitForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var email = document.getElementById("email").value;
    var phone_number = document.getElementById("phone").value;


    if (username == "" || password == "") {
      alert("Veuillez remplir tous les champs.");
    } else {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", "http://127.0.0.1:9000/registration/");
      xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
      xhr.onload = function() {
        if (xhr.status === 200) {
          var response = JSON.parse(xhr.responseText);
          
            alert("Authentification réussie !");
            window.location.href = "page4.html";
          } 
      };
      xhr.onerror = function() {
        alert("Une erreur est survenue.");
      };
      var params = "username=" + username + "&password=" + password + "&email=" + email + "&phone_number=" + phone_number;
      xhr.send(params);
    }
  }