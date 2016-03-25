/**
 * custom.min.js
 * @author Divay Prakash
 */

function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    document.getElementById('signout').style.display = 'inline';
    var id_token = googleUser.getAuthResponse().id_token;
}

function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function() { /*console.log('User signed out.');*/ });
    document.getElementById('signout').style.display = 'none';
}

function action() {
    document.getElementById('signout').style.display = 'none';
}