const birthdate = document.querySelector("input[name='birthdate']")
const conatinerPhoto = document.querySelector('#conatiner_photo')
const text = document.querySelector('#text')
const messageSuccess = document.querySelector('#message_success')


conatinerPhoto.children[2].classList.add('hidden')
conatinerPhoto.children[3].classList.add('hidden')
conatinerPhoto.children[4].classList.add('hidden')
conatinerPhoto.childNodes[4].textContent = ''
conatinerPhoto.childNodes[11].textContent = ''

if(messageSuccess){
    setTimeout(() => {
        messageSuccess.classList.add('hidden')
    }, 3000)
}
birthdate.setAttribute('type', 'date');
birthdate.classList.add('w-full', 'border', 'border-slate-300', 'bg-transparent', 'rounded-md', 'my-2')
