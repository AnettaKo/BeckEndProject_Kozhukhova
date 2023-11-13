// Define the base URL for the API
const apiUrl = "http://127.0.0.1:8000";

// Function to load all tasks from the server
async function loadTasks() {
  fetch(`${apiUrl}/my_wardrobe`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    },
  })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      // Add each task to the task list
      const listItems = document.getElementById('item-list');
      listItems.innerHTML = ""
      list_items = data._Wardrobe__list_items
      for (const itemId in list_items) {
        const item = list_items[itemId];
        let newItem = createArticleElement(item._Item__name, item.item_class, item.item_tipe, item.size, item.season, item.color, item.brand, item.price, item.description, itemId);

//        // const newTask = document.createElement("li");
//        // newTask.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center');
//        // newTask.innerHTML = `Title:${task.title}, Desc:${task.description}, Completed:${task.completed}
//        //       <div>
//        //           <button class="btn btn-sm btn-success mr-2" onclick="completeTask(${taskId})">Complete</button>
//        //           <button class="btn btn-sm btn-danger" onclick="deleteTask(${taskId})">Delete</button>
//        //       </div>`;
        listItems.appendChild(newItem);
      }
    })
    .catch(error => console.error('Error:', error));
}

// Load all tasks when the page is loaded
loadTasks();

// Function to create new task element
function createArticleElement(name, item_class, item_tipe, size, season, color, brand, price, description, id) {
  // Create a new list item
  let listItem = document.createElement('li');
  listItem.className = 'list-group-item d-flex justify-content-between align-items-center';

  // Create the task title element
  let articleTitle = document.createTextNode(name);

  // Create the task description element
  let articleDescription = document.createElement('small');
  articleDescription.className = 'text-muted ml-2';
  articleDescription.innerText = description;

//  // Create the task due date element
//  let taskDueDate = document.createElement('small');
//  taskDueDate.className = 'text-muted ml-2';
//  taskDueDate.innerText = due_date;

//  // Create the complete button element
//  let completeButton = document.createElement('button');
//  completeButton.className = 'btn btn-sm btn-success mr-2';
//  completeButton.innerText = 'Complete';
//  completeButton.addEventListener('click', function () {
//    completeTask(id, title, description, due_date);
//  });
//
//  // Create the delete button element
//  let deleteButton = document.createElement('button');
//  deleteButton.className = 'btn btn-sm btn-danger';
//  deleteButton.innerText = 'Delete';
//  deleteButton.addEventListener('click', function () {
//    deleteTask(id);
//  });

  // Add the task title, description, due date, complete button, and delete button elements to the list item
  listItem.appendChild(articleTitle);
  listItem.appendChild(articleDescription);
//  listItem.appendChild(taskDueDate);
//  if (!completed) {
//    listItem.appendChild(completeButton);
//  }
//  listItem.appendChild(deleteButton);


  // Return the list item element
  return listItem;
}