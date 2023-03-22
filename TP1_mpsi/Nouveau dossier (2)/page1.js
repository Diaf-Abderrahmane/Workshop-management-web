// function authenticate() {
//     var username = document.getElementById("username").value;
//     var password = document.getElementById("password").value;
//     if (username == "" || password == "") {
//         alert("Veuillez remplir tous les champs.");
//     } else {
//         // Effectuez ici la vérification de l'authentification avec le nom d'utilisateur et le mot de passe fournis
//         alert("Authentification réussie !");
//     }
// }
// function authenticate() {
//     var username = document.getElementById("username").value;
//     var password = document.getElementById("password").value;
//     if (username == "" || password == "") {
//       alert("Veuillez remplir tous les champs.");
//     } else {
//       var xhr = new XMLHttpRequest();
//       xhr.open("POST", "http://127.0.0.1:9000/login/");
//       xhr.setRequestHeader("Content-Type", "application/json");
//       xhr.onload = function() {
//         if (xhr.status === 200) {
//           var response = JSON.parse(xhr.responseText);
//           if (response.success) {
//             alert("Authentification réussie !");
//             window.location.href = "page3.html";
//           } else {
//             alert(response.message);
//           }
//         } else {
//           alert("Échec de l'authentification.");
//         }
//       };
//       xhr.onerror = function() {
//         alert("une erreur est survenue.");
       
//       };
//       xhr.send(JSON.stringify({
//         email: username,
//         password: password
//       }));
//     }
//   }


// function authenticate() {
//     var username = document.getElementById("username").value;
//     var password = document.getElementById("password").value;
//     if (username == "" || password == "") {
//         alert("Veuillez remplir tous les champs.");
//     } else {
//         // Effectuez ici la vérification de l'authentification avec le nom d'utilisateur et le mot de passe fournis
//         alert("Authentification réussie !");
//     }
// }
function authenticate() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if (username == "" || password == "") {
      alert("Veuillez remplir tous les champs.");
    } else {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", "http://127.0.0.1:9000/login/");
      xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
      xhr.onload = function() {
        if (xhr.status === 200) {
          var response = JSON.parse(xhr.responseText);
          
            alert("Authentification réussie !");
            window.location.href = "page4.html";
          } 
      };
      xhr.onerror = function() {
        alert("une erreur est survenue.");
      };
      var params = "username=" + username + "&password=" + password;
      xhr.send(params);
    }
  }



  function Créer() {
    var domaine = document.getElementById("Domaine").value;
    var DateDebute = document.getElementById("DateDebute").value;
    var DateFin = document.getElementById("DateFin").value;
    if ( domaine == "" || DateDebute == "" || DateFin == "" ) {
      alert("Veuillez remplir tous les champs.");
    } else {
      var xhr = new XMLHttpRequest();
      xhr.open("POST", "http://127.0.0.1:9000/add_work_shop/");
      xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
      xhr.onload = function() {
        if (xhr.status === 200) {
          var response = JSON.parse(xhr.responseText);
          
            
            window.location.href = "page8.html";
          } 
      };
      xhr.onerror = function() {
        alert("une erreur est survenue.");
      };
      var params = "domaine=" + domaine + "&DateDebute=" + DateDebute + "&DateFin=" + DateFin;
      xhr.send(params);
    }
  }  
  
  
  