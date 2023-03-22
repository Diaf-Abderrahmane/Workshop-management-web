const objectsList = document.getElementById('workshops-list');

fetch('http://127.0.0.1:9000/all_objects/')
  .then(response => response.json())
  .then(data => {
    data.forEach(object => {
      const li = document.createElement('li');
      li.innerHTML = `ID: ${object.pk}, Domaine: ${object.domaine}, DateDebute: ${object.DateDebute}, DateFin: ${object.DateFin}`;
      const button = document.createElement('button');
      button.setAttribute('id', 'show-member-btn'); 
      button.innerHTML = 'Afficher le membre';
      button.addEventListener('click', function() {
        window.location.href = `member.html?id=${object.pk}`;
      });
      li.appendChild(button);
      objectsList.appendChild(li);
    });
  })
  .catch(error => console.error(error));


// Ajout d'un gestionnaire d'événement pour le bouton "Créer un Work Chop"
document.getElementById("create-workshop-btn").addEventListener("click", function() {
  window.location.href = "page7.html";
});


// button.addEventListener('click', function() {
//   window.location.href = `member.html?id=${object.pk}`;
// });

