let slider = document.querySelector('.slider .list');
let items = document.querySelectorAll('.slider .list .item');
let next = document.getElementById('next');
let prev = document.getElementById('prev');
let dots = document.querySelectorAll('.slider .dots li');

let lengthItems = items.length - 1;
let active = 0;





function nextSide(){
    active = active + 1 <= lengthItems ? active + 1 : 0;
    reloadSlider();
}
next.onclick = nextSide;
function prevSide(){
    active = active - 1 >= 0 ? active - 1 : lengthItems;
    reloadSlider();
}
prev.onclick = prevSide;
isAutoSlide = true;
let refreshInterval = setInterval(()=> {
    if(isAutoSlide){
        next.click()
    }
    
}, 3000);
function reloadSlider(){
    //slider.style.marginLeft = -items[active].offsetLeft + 'px';
    slider.style.marginLeft = -items[active].offsetWidth * active + 'px';
    //
    let last_active_dot = document.querySelector('.slider .dots li.active');
    last_active_dot.classList.remove('active');
    dots[active].classList.add('active');

    clearInterval(refreshInterval);
    refreshInterval = setInterval(()=> {

        if(isAutoSlide){
            next.click()
        }
    }, 3000);


}
let startTouchX = 0; 
let endTouchX = 0;
slider.addEventListener('touchstart', (event) => {
    event.preventDefault();
    console.log('touchstart')
    isAutoSlide = false;
    startTouchX = event.changedTouches[0].pageX;
}, {capture: false, passive: false})
slider.addEventListener('touchend', (event) => {
    event.preventDefault();
    console.log('touschend')
    endTouchX = event.changedTouches[0].pageX;
    if( endTouchX > startTouchX){
        if( Math.abs(endTouchX - startTouchX) > 20){
            nextSide();
        }
    }
    if( endTouchX < startTouchX){
        if( Math.abs(endTouchX - startTouchX) > 20){
            prevSide();
        }
    }
    setTimeout(() => {
        isAutoSlide = true;
    }, 2000)
}, {capture: false, passive: false})

dots.forEach((li, key) => {
    li.addEventListener('click', ()=>{
         active = key;
         reloadSlider();
    })
})
window.onresize = function(event) {
    reloadSlider();
};


// const navLinkEls = document.querySelectorAll('.nav-list-link');


// navLinkEls.forEach(navLinkEl => {
//     navLinkEl.addEventListener('click', function() {
//         document.querySelector('.active')?.classList.remove('active');
//         this.classList.add('active');
//     });
// });



