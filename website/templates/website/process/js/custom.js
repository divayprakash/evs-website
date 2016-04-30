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

(function(i,s,o,g,r,a,m) {
	i['GoogleAnalyticsObject'] = r;
	i[r] = i[r] || function() {
		(i[r].q = i[r].q || []).push(arguments)}, i[r].l = 1 * new Date();
		a = s.createElement(o), m = s.getElementsByTagName(o)[0];
		a.async = 1;
		a.src = g;
		m.parentNode.insertBefore(a,m)
  })

(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-76075660-2', 'auto');
ga('send', 'pageview');
