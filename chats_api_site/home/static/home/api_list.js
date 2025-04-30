
document.addEventListener('DOMContentLoaded', () => {


//gestion du token csrf:
function getCSRFToken() {
   return  document.querySelector('meta[name="csrf_token"]').getAttribute('content');
}


    const csrfToken = getCSRFToken();

    const catList = document.getElementById('cat_list');
    const catForm = document.getElementById('cat_form');

    // variables du formulaire:
    const nameInput = document.getElementById('cat_name');
    const ageInput = document.getElementById('cat_age');



    function loadCats() {

        fetch('http://127.0.0.1:8000/cats/api_cat_list/')
        .then(response => response.json())
        .then(data => {

            // reset avant de recharger:
            catList.innerHTML = '';

            data.forEach( cat => {

                // ajout du label du chat
                const new_li = document.createElement('li');
                new_li.textContent = `name: ${cat.name}  //  age: ${cat.age}`;
                catList.append(new_li);

                // ajout du btn supprimer:
                const deleteBtn = document.createElement('button');
                deleteBtn.textContent = 'Delete';
                new_li.append(deleteBtn)
                deleteBtn.addEventListener('click', () => {
                    fetch(`http://127.0.0.1:8000/cats/api_cat_delete/${cat.id}/`, {
                        method: 'DELETE',
                        headers: {
                            'X-CSRFToken': csrfToken
                        }
                    })
                    .then(response => response.json())
                    .then(data => {
                        console.log(data.message)
                        loadCats() // recharge la liste après suppression
                    })
                    
                });
            });
        }); // fin then
    }; // fin func



    //////////////////
    ///// si submit:

    catForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const new_cat = {         // chat a ajouter queje recup du form
            name: nameInput.value,
            age: ageInput.value
        };


        fetch('http://127.0.0.1:8000/cats/api_cat_list/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(new_cat)
        })
        .then(response => response.json())
        .then(data => {

                console.log(`Ajout du chat: ${data}`)
                loadCats();
                catForm.reset()

            });
    }); // fin listener pour submit.














    //////////////
    /// lance et refresh:
    loadCats();
    setInterval(loadCats, 10000);
















}); // END ALL