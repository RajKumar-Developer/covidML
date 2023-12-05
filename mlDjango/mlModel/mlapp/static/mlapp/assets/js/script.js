document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.querySelector('.input');
    const button = document.querySelector('.button');
    
    fileInput.addEventListener('change', function() {
        const fileList = this.files;
        const outputList = document.querySelector('.output-list');
        
        outputList.innerHTML = ''; // Clear previous entries
        
        for (const file of fileList) {
            const listItem = document.createElement('li');
            listItem.textContent = file.name;
            outputList.appendChild(listItem);
        }
        
        // Enable the button if files are selected
        button.disabled = !(fileList.length > 0);
        
        // Stop animation
        const inputDiv = document.querySelector('.input-div');
        inputDiv.style.animation = 'none';
    });
});


document.querySelector('.input').addEventListener('change', function() {
    var fileName = this.value.split('\\').pop(); // Get the file name
    var inputDiv = document.querySelector('.input-div');
    
    // Check if a file has been selected
    if (fileName) {
        inputDiv.style.borderColor = 'green'; // Change border color to green
        inputDiv.style.boxShadow = '0px 0px 100px green, inset 0px 0px 10px green, 0px 0px 5px #ffffff'; // Change box shadow
        
        // Enable the button
        document.querySelector('.button').disabled = false;
    }
});
