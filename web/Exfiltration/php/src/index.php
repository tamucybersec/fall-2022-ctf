<?php
$result = NULL;

if(isset($_POST['input'])) {
    handle_post();
}

function handle_post() {
    $servername = "db";
    $username = "ro_user";
    $password = "9b31dcc8229d2ed5519a7e4072bdba66";
    $db_name = "users";

    $conn = new mysqli($servername, $username, $password, $db_name);

    if($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = "SELECT username,phone,email,id FROM users.users WHERE username LIKE '%{$_POST['input']}%';";
    global $result;
    $result = $conn->query($sql);

    $conn->close();
}
?>

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="/css/style.css">
    <title>Exfiltration-TAMUctf</title>
</head>
<body>
    <header class="site-header">
        <div class="header-content">
            <a class="site-title" href="/">User Search</a>
            <nav class="nav-bar">
                <a class="page-link" href="https://github.com/tamuctf">
                    <img class="icon" src="/img/github.png" alt>
                    Github
                </a>
            </div>
        </div>
    </header>
    <main class="page-content">
        <div class="wrapper">
            <center>
                <div class="search-bar">
                    <form action="/index.php" method="post">
                        <input class="input" type="text" id="input" name="input" placeholder="User Search...">
                    </form>
                </div>
<?php
$results = array();

if (isset($result) && !empty($result->num_rows) && $result->num_rows > 0) {
    array_push($results, '<table class="results">');
    array_push($results, '<tr><th>Username</th><th>Phone</th><th>Email</th><th>ID Number</th></tr><tr>');
    while($row = $result->fetch_assoc()) {
        array_push($results, "<tr><td>{$row['username']}</td><td>{$row['phone']}</td><td>{$row['email']}</td><td>{$row['id']}</td></tr>");
    }
    array_push($results, '</table>');
    for($i = 0; $i < count($results); $i++) {
        echo $results[$i];
    }
} else {
    echo '<p style="margin-top:20px;color:#222222">0 Results</p>';
}
?>
            </center>
        </div>
    </main>
</body>
<html>

