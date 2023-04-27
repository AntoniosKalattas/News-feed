const {spawn} = require('child-process')

const pyscript = spawn('python', ['main.py'])
pyscript.stdout.on('data', (data)=>{
    console.log(data);
    let python_output = data;
})

function add_element(){
    const article = document.createElement('article')
    article.innerHTML = `<p id="article">$pythonouput</p>`
}