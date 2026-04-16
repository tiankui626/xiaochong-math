$content = [System.IO.File]::ReadAllText("C:\Users\hp\.openclaw\workspace\skills\math-course-manager\SKILL.md", [System.Text.Encoding]::UTF8)
$content | Out-File -FilePath "C:\Users\hp\xiaochong-math\temp_new_skill.md" -Encoding UTF8
git -C "C:\Users\hp\xiaochong-math" add "temp_new_skill.md"
git -C "C:\Users\hp\xiaochong-math" mv ".skills/math-course-manager/SKILL.md" ".skills/math-course-manager/SKILL.md.bak"
git -C "C:\Users\hp\xiaochong-math" rm --cached ".skills/math-course-manager/SKILL.md"
git -C "C:\Users\hp\xiaochong-math" mv "temp_new_skill.md" ".skills/math-course-manager/SKILL.md"
git -C "C:\Users\hp\xiaochong-math" rm ".skills/math-course-manager/SKILL.md.bak" 2>$null
git -C "C:\Users\hp\xiaochong-math" add ".skills/math-course-manager/SKILL.md"
git -C "C:\Users\hp\xiaochong-math" commit -m "fix: replace corrupted SKILL.md blob with correct UTF-8 content"
git -C "C:\Users\hp\xiaochong-math" push
echo "done"
