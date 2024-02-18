document.addEventListener('DOMContentLoaded', function () {
    function cngclr(){
        var btn = document.getElementById("todo-btn");
        btn.style.backgroundColor= '#8EACCD';
    };
    
    
    
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
            todo.classList.add('td-itm');
    
            const todo_cont = document.getElementById('list-container');
            todo_cont.appendChild(todo);
            let span = document.createElement("span");
            span.innerHTML = "\u00d7";
            todo.appendChild(span);


            fetch('/addtodo',{
                method: 'POST',
                headers: {
                    'Content-type': 'application/json',
                },
                body: JSON.stringify({task:todo_text}),

            })
            
    
        }
    
    
    function change_status(){
    
        listContainer = document.getElementById('list-container');
    
        listContainer.addEventListener("click",function(e){
            if(e.target.tagName === "LI"){
                e.target.classList.toggle("checked");
            }
            else if(e.target.tagName === "SPAN"){
                e.target.parentElement.remove();
                text = e.target.parentElement.innerText;
                text = text.replace('\u00d7','');
                text = text.trim();
                delete_todo(text);
            }
        })
    }
    function delete_todo(text){
            fetch('/deletetodo',{
                method: 'POST',
                headers: {
                    'Content-type': 'application/json',
                },
                body: JSON.stringify({task:text}),

            })

    }
    btn.addEventListener("click",add_todo);
    listContainer = document.getElementById('list-container');
    listContainer.addEventListener("click",change_status);
    

});







//https://stackoverflow.com/questions/6396101/pure-javascript-send-post-data-without-a-form 