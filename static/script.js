




function cngclr(){
    var btn = document.getElementById("todo-btn");
    btn.style.backgroundColor= '#8EACCD';
}



var btn = document.getElementById("todo-btn");

btn.addEventListener("mousedown",cngclr)
btn.addEventListener("mouseup",function(){
    btn.style.backgroundColor= '#cae1e5a3';
})

function add_todo(){


        const todo_text = document.getElementById('todo-input').value;
        if (todo_text == ''){
            return 0;
        }



        const todo = document.createElement('li');
        todo.innerText = todo_text;
        todo.classList.add('list-itm');

        const todo_cont = document.getElementById('list-container');
        todo_cont.appendChild(todo);
        


