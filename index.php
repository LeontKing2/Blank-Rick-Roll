<?php
header("Refresh: 5; url=https://www.youtube.com/watch?v=dQw4w9WgXcQ");

// Get the user agent
$user_agent = strtolower($_SERVER['HTTP_USER_AGENT']);

// Check if browser is Firefox-based
$is_firefox_based = strpos($user_agent, 'firefox') !== false;

if ($is_firefox_based) {
    // Firefox: Use Link header
    header('Link: <style.css>; rel=stylesheet;');
} else {
    // Chrome/Others: Use HTML link element
    require(style.php);
}
?>
