
document.addEventListener('DOMContentLoaded', () => {
    const birthdate = document.querySelector("input[name='birthdate']")
    const img_container = document.querySelector('#img_container')
    const image_label = document.querySelector('#id_image_label')
    const messageSuccess = document.querySelector('#message_success')
    const form = document.querySelector('form')
    
    const img = document.createElement('img')
    
    if ( form.children[3].getAttribute('href')) {
        
        img.setAttribute('src', form.children[3].getAttribute('href'))
        img.classList.add('w-full', 'object-contain', 'h-[100px]', 'mx-auto')
        image_label.classList.add('mt-[3rem]')
        img_container.appendChild(img)
    }

    form.children[5].classList.add('hidden')
    form.children[6].classList.add('hidden')

    form.childNodes[15].textContent = ''

    if (messageSuccess) {
        setTimeout(() => {
            messageSuccess.classList.add('hidden')
        }, 3000)
    }
    birthdate.setAttribute('type', 'date');
    birthdate.classList.add('w-full', 'border', 'border-slate-300', 'bg-transparent', 'rounded-md', 'my-2')


})