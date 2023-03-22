const objectsList = document.getElementById('objectsList');

fetch('http://127.0.0.1:9000/all_objects/')
  .then(response => response.json())
  .then(data => {
    data.forEach(object => {
      const li = document.createElement('li');
      li.innerHTML = `PK: ${object.pk}, Marque: ${object.marque}, Modèle: ${object.modele}, Acceleration: ${object.acceleration}, Sièges: ${object.seat}, Prix: ${object.price}`;
      objectsList.appendChild(li);
    });
  })
  .catch(error => console.error(error));
