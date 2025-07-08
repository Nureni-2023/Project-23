<?php
// save_score.php

$data = json_decode(file_get_contents('php://input'), true);
$score = $data['score'];

// Save the score to a text file (or use a database in a real application)
file_put_contents("scores.txt", "Score: $score\n", FILE_APPEND);

echo json_encode(["message" => "Score saved successfully", "score" => $score]);
?>
