<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="static/style.css">
        <title>TAMUctf-Included</title>
    </head>
    <body>
        <header class="site-header">
            <div class="header-content">
                <a class="site-title" rel="author" href="/">Included</a>
                <nav class="site-nav">
                </nav>
            </div>
        </header>
        <main class="page-content">
            <center>
<?php
if(!isset($_GET['file'])) {
    echo "<h1>Nothing to see here!</h1>";
} else {
    include($_GET['file']);
}
?>
            <center>
        </main>
    </body>
</html>
