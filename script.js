/*$('.pro-container').slick({
    centerMode: true,
    centerPadding: '60px',
    slidesToShow: 3,
    responsive: [{
            breakpoint: 768,
            settings: {
                arrows: false,
                centerMode: true,
                centerPadding: '40px',
                slidesToShow: 3
            }
        },
        {
            breakpoint: 480,
            settings: {
                arrows: false,
                centerMode: true,
                centerPadding: '40px',
                slidesToShow: 1
            }
        }
    ]
});*/
// Get the button:
let mybutton = document.getElementsByClassName("btn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}


$('.slider').slick({
    dots: false,
    infinite: false,
    arrows: false,
    speed: 300,
    autoplay: true,
    slidesToShow: 6,
    slidesToScroll: 6,
    responsive: [{
            breakpoint: 991,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 3,
                infinite: true,
            }
        },
        {
            breakpoint: 600,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2
            }
        },
        {
            breakpoint: 480,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }
        // You can unslick at a given breakpoint now by adding:
        // settings: "unslick"
        // instead of a settings object
    ]
});
$('.banner-img').slick({
    dots: false,
    infinite: false,
    arrows: false,
    speed: 300,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
});
const scriptURL = 'https://script.google.com/u/0/home/projects/10nnJs5rZ1YVFw5Es4SkkSWC73oE-6DJTo583Oa6P5p8e1PBHPBJIwz_X/edit'
const form = document.forms['submit-to-google-sheet']
const msg = document.getElementById("msg")

form.addEventListener('Sign up', e => {
    e.preventDefault()
    fetch(scriptURL, { method: 'POST', body: new FormData(form) })
        .then(response => {
            msg.outerHTML = "Message sent successfully"
            setTimeout(function() {
                msg.outerHTML = "Successful Login"
            }, 5000)
            form.reset()
        })
        .catch(error => console.error('Error!', error.message))
})

// JavaScript to toggle the dropdown menu
document.addEventListener("DOMContentLoaded", function() {
    const dropdownBtn = document.querySelector(".dropbtn");
    const dropdownContent = document.querySelector(".dropdown-content");

    dropdownBtn.addEventListener("click", function() {
        dropdownContent.classList.toggle("show");
    });

    window.addEventListener("click", function(event) {
        if (!event.target.matches('.dropbtn')) {
            const dropdowns = document.getElementsByClassName("dropdown-content");
            for (let i = 0; i < dropdowns.length; i++) {
                const openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
                }
            }
        }
    });
});

// For chat between users
function chatbox(organiser, client) {
    while (true) {
        const user1Input = prompt(`${organiser}:`);
        if (user1Input.toLowerCase() === 'exit' || user1Input.toLowerCase() === 'quit') {
            break;
        }

        const user2Input = prompt(`${client}:`);
        if (user2Input.toLowerCase() === 'exit' || user2Input.toLowerCase() === 'quit') {
            break;
        }
    }
}

// Main code
const user1Name = prompt("Enter User 1's name:");
const user2Name = prompt("Enter User 2's name:");
chatbox(user1Name, user2Name);