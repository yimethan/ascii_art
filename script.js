document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            // Display the image in an img tag
            const img = document.createElement('img');
            img.src = e.target.result;
            img.style.maxWidth = '100%';
            img.style.height = 'auto';

            // Clear any previous image
            const imagePreview = document.getElementById('imagePreview');
            imagePreview.innerHTML = '';
            imagePreview.appendChild(img);
        };
        reader.readAsDataURL(file);
    }
});
