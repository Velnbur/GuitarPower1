
$(document).ready(function(){
    $(".header").sticky();
    document.querySelector('.nav-list-hamburger').style.display = "none";

    $('.fullscreen').css('height', window.innerHeight);
    $('.halfscreen').css('height', window.innerHeight*0.6);
/*    var sliderOne = slideShow('.slider', { isAutoplay: true });
    var sliderOne = slideShow('.comment-article-slider', { isAutoplay: true });*/

    if(document.querySelector('.forum-unit-post-img')) {
        document.querySelectorAll('.forum-unit-post-img').forEach(function(element) {
            if (element.height >= element.width) {
                element.style.height = '100%';
                element.style.width = 'auto';
            }
            element.parentNode.childNodes[1].childNodes[1].src = element.src;
        });
    }
    if(document.querySelector('.mouse-parallax-bg')) {
        $(function(){
            $('.mouse-parallax-bg').parallax({
                mouseport: $('.forum-intro-section'),
                decay: 0.9
            });

        });
    }
});

window.addEventListener("resize", function() {
//    ======== START For hamburger anim, HEADER  1 ==============//
    if($('.nav-list').css('display') == 'block') {
        document.querySelector('.nav-list-hamburger').style.display = 'none';
        document.querySelector('#hamburger_anim').classList.value = 'ham hamRotate ham1';
    }
//    ======== END For hamburger anim, HEADER  1 ==============//
});


//    ======== START For hamburger anim, HEADER  2 ==============//
function hamburger() {
    var i = document.querySelector('.nav-list-hamburger');
    if(i.style.display == "none") {
        i.style.display = "block";
    }
    else {
        i.style.display = "none";
    }
}
//    ======== END For hamburger anim, HEADER  2 ==============//

if (document.querySelectorAll('.flying-inscription')) {
    document.querySelectorAll('.flying-inscription').forEach(function(element) {
        element.addEventListener('mouseover', function(event) {

            var elements = [];
            var text = event.target.parentNode.querySelector('.flying-inscription-text-box');

            document.querySelectorAll('.flying-inscription').forEach(el => {if(el != event.target) elements.push(el)});

            event.target.style.opacity = 0;
            var anim = setInterval(function() {
                if (Number(elements[0].style.opacity) >= 0.4) {
                    clearInterval(anim);
                }

                elements.forEach(function(el) {
                    el.style.opacity = Number(el.style.opacity) + 0.1;
                    text.style.opacity = Number(text.style.opacity) + 0.2;
                });
            }, 20);

            element.addEventListener('mouseout', function(event) {
                clearInterval(anim)
                document.querySelectorAll('.flying-inscription').forEach(el => {el.style.opacity = 0});
                text.style.opacity = 0;
            });
        });
    });
}


/*
function headerAnimation() {
    console.log(window.scrollY);
    if(window.scrollY >= 40) {
        document.querySelector('.sticky-wrapper').cssText = 'top: 0;';
    }
}
*/
