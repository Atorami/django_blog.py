document.addEventListener('DOMContentLoaded', function (event) {
    let input_data = document.getElementById('searchbar').value;
        if(input_data === 'None'){
            document.getElementById('searchbar').value = ''
        }
})