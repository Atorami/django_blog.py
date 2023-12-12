document.addEventListener('DOMContentLoaded', function (event) {
    let input_data = document.getElementById('searchbar').value;
        if(input_data === 'None'){
            document.getElementById('searchbar').value = ''
        }
    const snow_background = document.querySelector('.weather_wrapper')

const startSnowing = () =>{
    const snow = document.createElement('span')
    snow.className = 'snow'

    const minSize = 5;
    const maxSize = 10;


    let snowSize = Math.random()*(maxSize-minSize) + minSize

    snow.style.width = snowSize + 'px'
    snow.style.height = snowSize + 'px'

    snow.style.left = Math.random()*100+'%'

    snow_background.appendChild(snow)

    setTimeout(() =>{
        snow.remove()
    }, 1400)
}

setInterval(startSnowing, 100)
})

