const image1 = document.querySelector('.img1');
const image2 = document.querySelector('.img2');

image1.addEventListener('click',function() {
    image2.src = "";
});
image2.addEventListener('click',function() {
    image1.src = "";
});