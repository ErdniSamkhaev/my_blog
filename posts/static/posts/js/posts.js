// posts.js
document.addEventListener("DOMContentLoaded", function() {
    const images = ['image1.jpg', 'image2.jpg', 'image3.jpg'];
    let currentImageIndex = 0;

    const carouselImg = document.getElementById('carouselImg');

    setInterval(() => {
        currentImageIndex = (currentImageIndex + 1) % images.length;
        carouselImg.src = images[currentImageIndex];
    }, 3000);
});
