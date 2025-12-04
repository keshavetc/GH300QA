"""
GitHub Copilot 300 Q&A Generator
Generates comprehensive HTML files for remaining topics (5-11)
"""

import os
from pathlib import Path
from datetime import datetime

# Base directory - current directory since script is in GH_300Q&A folder
OUTPUT_DIR = Path(".")

# Common CSS and structure
def get_html_template(topic_num, title, subtitle, qa_count, prev_topic, next_topic):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - GitHub Copilot Q&A</title>
    <style>
        * {{margin: 0; padding: 0; box-sizing: border-box;}}
        body {{font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; background: #f5f7fa; padding: 20px;}}
        .container {{max-width: 1000px; margin: 0 auto; background: white; border-radius: 10px; box-shadow: 0 5px 20px rgba(0,0,0,0.1); overflow: hidden;}}
        header {{background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px;}}
        header h1 {{font-size: 2em; margin-bottom: 10px;}}
        .nav-links {{padding: 15px 30px; background: #f8f9fa; border-bottom: 2px solid #e9ecef;}}
        .nav-links a {{color: #667eea; text-decoration: none; margin-right: 20px; font-weight: 500;}}
        .nav-links a:hover {{text-decoration: underline;}}
        .content {{padding: 40px;}}
        .qa-item {{margin-bottom: 30px; border-left: 4px solid #667eea; padding-left: 20px;}}
        .question {{font-weight: 600; font-size: 1.1em; color: #2d3748; margin-bottom: 10px; cursor: pointer; display: flex; align-items: center; gap: 10px;}}
        .question::before {{content: 'Q'; background: #667eea; color: white; width: 30px; height: 30px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0;}}
        .answer {{margin-left: 40px; padding: 15px; background: #f8f9fa; border-radius: 8px; margin-top: 10px;}}
        .answer::before {{content: 'A: '; font-weight: bold; color: #667eea;}}
        .answer ul, .answer ol {{margin-left: 20px; margin-top: 10px;}}
        .answer li {{margin-bottom: 5px;}}
        .code-block {{background: #2d3748; color: #68d391; padding: 15px; border-radius: 5px; margin: 10px 0; overflow-x: auto; font-family: 'Courier New', monospace; font-size: 0.85em; line-height: 1.4;}}
        .highlight {{background: #fef3c7; padding: 2px 6px; border-radius: 3px; font-weight: 500;}}
        .info-box {{background: #dbeafe; border-left: 4px solid #3b82f6; padding: 15px; margin: 10px 0; border-radius: 5px;}}
        .warning-box {{background: #fef3c7; border-left: 4px solid #f59e0b; padding: 15px; margin: 10px 0; border-radius: 5px;}}
        footer {{background: #2d3748; color: white; text-align: center; padding: 20px;}}
        @media print {{body {{background: white;}} .nav-links {{display: none;}} .qa-item {{page-break-inside: avoid;}}}}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </header>

        <div class="nav-links">
            <a href="index.html">← Back to Hub</a>
            {f'<a href="{prev_topic}">← Previous</a>' if prev_topic else ''}
            {f'<a href="{next_topic}">Next Topic →</a>' if next_topic else ''}
        </div>

        <div class="content">
"""

def get_footer(topic_num):
    return """        </div>

        <footer>
            <p>GitHub Copilot Q&A - Topic {topic_num} of 11 | © 2025</p>
        </footer>
    </div>

    <script>
        document.querySelectorAll('.question').forEach(question => {{
            question.addEventListener('click', function() {{
                const answer = this.nextElementSibling;
                answer.style.display = answer.style.display === 'none' ? 'block' : 'none';
            }});
        }});
    </script>
</body>
</html>""".format(topic_num=topic_num)

def qa_item(question, answer):
    return f"""            <div class="qa-item">
                <div class="question">{question}</div>
                <div class="answer">
                    {answer}
                </div>
            </div>

"""

# Topic 5: CLI Commands & Limitations
def generate_topic_05():
    qa_list = [
        ("What is the GitHub Copilot CLI?", """
                    The GitHub Copilot CLI (Command Line Interface) is an extension for the GitHub CLI (gh) that brings AI assistance to your terminal. It provides:
                    <ul>
                        <li><strong>Natural language to command:</strong> Convert plain English to shell commands</li>
                        <li><strong>Git command help:</strong> Assistance with complex git operations</li>
                        <li><strong>Command explanation:</strong> Understand what commands do</li>
                        <li><strong>Script generation:</strong> Create shell scripts from descriptions</li>
                    </ul>
                    <strong>Availability:</strong> GitHub Copilot Individual and Enterprise (limited in Business)
        """),
        
        ("How do you install the GitHub Copilot CLI extension?", """
                    <strong>Installation steps:</strong>
                    <ol>
                        <li><strong>Install GitHub CLI:</strong> Download from https://cli.github.com</li>
                        <li><strong>Authenticate:</strong> <code>gh auth login</code></li>
                        <li><strong>Install Copilot extension:</strong>
                            <div class="code-block">gh extension install github/gh-copilot</div>
                        </li>
                        <li><strong>Verify installation:</strong>
                            <div class="code-block">gh copilot --version</div>
                        </li>
                    </ol>
                    <strong>Requirements:</strong>
                    <ul>
                        <li>GitHub CLI v2.0.0 or later</li>
                        <li>Active GitHub Copilot subscription</li>
                        <li>Authenticated GitHub account</li>
                    </ul>
        """),
        
        ("What are the main GitHub Copilot CLI commands?", """
                    <strong>Core commands:</strong>
                    <div class="code-block">
# Suggest shell commands<br>
gh copilot suggest "list all files modified in last 7 days"<br>
<br>
# Explain commands<br>
gh copilot explain "tar -xzf file.tar.gz"<br>
<br>
# Interactive mode<br>
gh copilot<br>
<br>
# Get help<br>
gh copilot --help
                    </div>
                    <strong>Aliases (shorter commands):</strong>
                    <div class="code-block">
ghcs "your query"  # suggest<br>
ghce "command"     # explain
                    </div>
        """),
        
        ("How does 'gh copilot suggest' work?", """
                    <code>gh copilot suggest</code> converts natural language descriptions into executable shell commands.
                    <br><br>
                    <strong>Examples:</strong>
                    <div class="code-block">
# Find large files<br>
$ gh copilot suggest "find files larger than 100MB"<br>
→ find . -type f -size +100M<br>
<br>
# Process management<br>
$ gh copilot suggest "kill all node processes"<br>
→ pkill -9 node<br>
<br>
# Git operations<br>
$ gh copilot suggest "undo last commit but keep changes"<br>
→ git reset --soft HEAD~1
                    </div>
                    <strong>Features:</strong>
                    <ul>
                        <li>Multiple suggestions provided</li>
                        <li>Interactive selection</li>
                        <li>Direct execution option</li>
                        <li>Explanation of suggested commands</li>
                    </ul>
        """),
        
        ("How does 'gh copilot explain' work?", """
                    <code>gh copilot explain</code> provides detailed explanations of shell commands and their options.
                    <br><br>
                    <strong>Example:</strong>
                    <div class="code-block">
$ gh copilot explain "docker run -d -p 8080:80 nginx"<br>
<br>
Explanation:<br>
- docker run: Create and start a container<br>
- -d: Run container in detached mode (background)<br>
- -p 8080:80: Map port 8080 on host to port 80 in container<br>
- nginx: Use nginx image from Docker Hub
                    </div>
                    <strong>Use cases:</strong>
                    <ul>
                        <li>Learning new commands</li>
                        <li>Understanding legacy scripts</li>
                        <li>Security review of commands before execution</li>
                        <li>Documentation for team members</li>
                    </ul>
        """),
        
        ("What types of commands can GitHub Copilot CLI generate?", """
                    <strong>Supported command categories:</strong>
                    <ul>
                        <li><strong>Shell/Bash:</strong> File operations, text processing, system admin</li>
                        <li><strong>Git:</strong> Version control, branching, merging, rebasing</li>
                        <li><strong>Docker:</strong> Container management, image operations</li>
                        <li><strong>Package managers:</strong> npm, pip, apt, brew commands</li>
                        <li><strong>System administration:</strong> User management, permissions, processes</li>
                        <li><strong>Network:</strong> curl, wget, ssh, scp operations</li>
                        <li><strong>Data processing:</strong> awk, sed, grep, jq</li>
                    </ul>
                    <strong>Platform support:</strong> Linux, macOS, Windows (PowerShell/WSL)
        """),
        
        ("What are the limitations of GitHub Copilot CLI?", """
                    <strong>Current limitations:</strong>
                    <ul>
                        <li><strong>Context awareness:</strong> Limited understanding of your specific environment</li>
                        <li><strong>Custom aliases:</strong> Doesn't know your personal shell aliases</li>
                        <li><strong>Complex workflows:</strong> May struggle with multi-step operations</li>
                        <li><strong>Platform differences:</strong> Commands may need adjustment between OS</li>
                        <li><strong>Security:</strong> Cannot verify if suggested commands are safe for your system</li>
                        <li><strong>API-dependent:</strong> Requires internet connection</li>
                        <li><strong>No execution validation:</strong> Doesn't check if files/paths exist</li>
                    </ul>
                    <div class="warning-box">
                        <strong>⚠️ Always review commands before execution, especially those that modify system state or data.</strong>
                    </div>
        """),
        
        ("Can GitHub Copilot CLI access your file system?", """
                    <strong>No</strong>, GitHub Copilot CLI has <strong>limited local context:</strong>
                    <ul>
                        <li>❌ Cannot read your files or directories</li>
                        <li>❌ Doesn't know your current directory structure</li>
                        <li>❌ Cannot verify file existence before suggesting commands</li>
                        <li>✅ Uses only the text you provide in queries</li>
                    </ul>
                    <strong>Implication:</strong> You need to provide context in your queries:
                    <div class="code-block">
# Less specific (may get generic answer)<br>
gh copilot suggest "compile the code"<br>
<br>
# More specific (better results)<br>
gh copilot suggest "compile Java code in src/ to build/ using Maven"
                    </div>
        """),
        
        ("How do you use GitHub Copilot CLI in scripts?", """
                    <strong>Scripting approaches:</strong>
                    <br><br>
                    <strong>1. Generate commands non-interactively:</strong>
                    <div class="code-block">
# Get suggestion without interactive prompt<br>
gh copilot suggest --non-interactive "compress all log files"
                    </div>
                    <strong>2. Pipe to shell execution (use with caution):</strong>
                    <div class="code-block">
# NOT RECOMMENDED - executes without review<br>
gh copilot suggest "clean temp files" | sh
                    </div>
                    <strong>3. Better approach - save and review:</strong>
                    <div class="code-block">
gh copilot suggest "backup database" > backup_cmd.sh<br>
cat backup_cmd.sh  # Review<br>
sh backup_cmd.sh   # Execute after review
                    </div>
                    <div class="warning-box">
                        <strong>Security Warning:</strong> Never blindly execute AI-generated commands in production scripts.
                    </div>
        """),
        
        ("What shell environments does GitHub Copilot CLI support?", """
                    <strong>Supported shells:</strong>
                    <ul>
                        <li>✅ <strong>Bash</strong> (Linux, macOS, WSL)</li>
                        <li>✅ <strong>Zsh</strong> (macOS default, Linux)</li>
                        <li>✅ <strong>PowerShell</strong> (Windows, cross-platform)</li>
                        <li>✅ <strong>Fish</strong></li>
                        <li>⚠️ <strong>Cmd.exe</strong> (limited support)</li>
                    </ul>
                    <strong>Configuration:</strong> Copilot CLI adapts suggestions based on detected shell, but you can specify:
                    <div class="code-block">
gh copilot suggest --shell bash "find duplicate files"<br>
gh copilot suggest --shell powershell "list running services"
                    </div>
        """),
        
        ("Can GitHub Copilot CLI generate multi-line scripts?", """
                    <strong>Yes</strong>, but with varying complexity:
                    <br><br>
                    <strong>Simple scripts work well:</strong>
                    <div class="code-block">
$ gh copilot suggest "create script to backup and compress logs"<br>
<br>
#!/bin/bash<br>
DATE=$(date +%Y%m%d)<br>
tar -czf logs_backup_$DATE.tar.gz /var/log/<br>
mv logs_backup_$DATE.tar.gz /backups/
                    </div>
                    <strong>Complex scripts may need iteration:</strong>
                    <ul>
                        <li>Break complex tasks into smaller queries</li>
                        <li>Generate sections separately</li>
                        <li>Combine and refine manually</li>
                    </ul>
                    <strong>Tip:</strong> For complex automation, IDE Copilot (in VS Code) is better suited than CLI.
        """),
        
        ("How does GitHub Copilot CLI handle errors in suggested commands?", """
                    <strong>Error handling capabilities:</strong>
                    <ul>
                        <li><strong>Syntax checking:</strong> Suggests syntactically valid commands</li>
                        <li><strong>No runtime validation:</strong> Cannot predict execution errors</li>
                        <li><strong>No rollback:</strong> Cannot undo executed commands</li>
                        <li><strong>Learning:</strong> Can refine suggestions if you provide feedback</li>
                    </ul>
                    <strong>Best practices:</strong>
                    <ol>
                        <li>Test commands in safe environment first</li>
                        <li>Use <code>--dry-run</code> flags when available</li>
                        <li>Review explanations before execution</li>
                        <li>Keep backups for destructive operations</li>
                    </ol>
        """),
        
        ("Can you use GitHub Copilot CLI offline?", """
                    <strong>No</strong>, GitHub Copilot CLI requires:
                    <ul>
                        <li>❌ Active internet connection</li>
                        <li>❌ GitHub API access</li>
                        <li>❌ Valid authentication token</li>
                    </ul>
                    <strong>Why:</strong>
                    <ul>
                        <li>Commands are generated by cloud-based AI models</li>
                        <li>No local model available</li>
                        <li>Requires real-time API communication</li>
                    </ul>
                    <strong>Alternative:</strong> For offline command help, use:
                    <ul>
                        <li><code>man</code> pages</li>
                        <li><code>--help</code> flags</li>
                        <li><code>tldr</code> (simplified man pages)</li>
                    </ul>
        """),
        
        ("How do you customize GitHub Copilot CLI behavior?", """
                    <strong>Configuration options:</strong>
                    <div class="code-block">
# Set default shell<br>
gh copilot config set shell bash<br>
<br>
# Set interaction mode<br>
gh copilot config set mode interactive<br>
<br>
# View current config<br>
gh copilot config list
                    </div>
                    <strong>Environment variables:</strong>
                    <div class="code-block">
# Adjust verbosity<br>
export GH_COPILOT_VERBOSE=1<br>
<br>
# Set timeout<br>
export GH_COPILOT_TIMEOUT=30
                    </div>
                    <strong>Limitations:</strong> Cannot train on your specific command patterns or create custom command libraries.
        """),
        
        ("What is the difference between GitHub Copilot CLI and IDE Copilot?", """
                    <strong>GitHub Copilot CLI:</strong>
                    <ul>
                        <li>Terminal/command-line focused</li>
                        <li>Shell command generation and explanation</li>
                        <li>System administration tasks</li>
                        <li>Git command assistance</li>
                        <li>Quick one-off commands</li>
                    </ul>
                    <strong>IDE Copilot (VS Code, etc.):</strong>
                    <ul>
                        <li>Code editor integration</li>
                        <li>Programming language code generation</li>
                        <li>Multi-file context awareness</li>
                        <li>Inline code completion</li>
                        <li>Complex application development</li>
                    </ul>
                    <strong>Complementary:</strong> Use both together - IDE for development, CLI for operations.
        """),
        
        ("Can GitHub Copilot CLI help with Git operations?", """
                    <strong>Yes!</strong> Git is a primary use case:
                    <br><br>
                    <strong>Common Git queries:</strong>
                    <div class="code-block">
gh copilot suggest "undo last commit keeping changes"<br>
→ git reset --soft HEAD~1<br>
<br>
gh copilot suggest "delete remote branch"<br>
→ git push origin --delete branch-name<br>
<br>
gh copilot suggest "show files changed in last commit"<br>
→ git diff --name-only HEAD~1 HEAD<br>
<br>
gh copilot suggest "interactive rebase last 5 commits"<br>
→ git rebase -i HEAD~5<br>
<br>
gh copilot suggest "cherry pick commit from another branch"<br>
→ git cherry-pick &lt;commit-hash&gt;
                    </div>
                    <strong>Especially useful for:</strong>
                    <ul>
                        <li>Complex rebase operations</li>
                        <li>Submodule management</li>
                        <li>Advanced git log queries</li>
                        <li>Git configuration</li>
                    </ul>
        """),
        
        ("How does GitHub Copilot CLI handle dangerous commands?", """
                    <strong>Safety measures:</strong>
                    <ul>
                        <li><strong>Warning display:</strong> Shows command before execution</li>
                        <li><strong>Confirmation prompt:</strong> Asks "Execute this command?"</li>
                        <li><strong>Explanation available:</strong> Review what command does</li>
                    </ul>
                    <div class="warning-box">
                        <strong>⚠️ No automatic blocking:</strong> Copilot CLI will suggest potentially destructive commands if requested. Examples:
                        <ul>
                            <li><code>rm -rf /</code> - Deletes all files</li>
                            <li><code>dd if=/dev/zero of=/dev/sda</code> - Wipes disk</li>
                            <li><code>:(){ :|:& };:</code> - Fork bomb</li>
                        </ul>
                    </div>
                    <strong>Your responsibility:</strong>
                    <ul>
                        <li>Understand commands before executing</li>
                        <li>Test in safe environments</li>
                        <li>Use <code>gh copilot explain</code> first</li>
                        <li>Never blindly copy-paste</li>
                    </ul>
        """),
        
        ("Can GitHub Copilot CLI learn from your command history?", """
                    <strong>No</strong>, Copilot CLI does not:
                    <ul>
                        <li>❌ Access your shell history</li>
                        <li>❌ Learn from your past commands</li>
                        <li>❌ Customize to your patterns</li>
                        <li>❌ Remember previous interactions</li>
                    </ul>
                    <strong>Each query is stateless:</strong> Every suggestion is generated independently without context from previous sessions.
                    <br><br>
                    <strong>Workaround:</strong> Provide context in your queries:
                    <div class="code-block">
# Less helpful<br>
gh copilot suggest "do the usual deployment"<br>
<br>
# More helpful<br>
gh copilot suggest "deploy Node.js app to AWS using Docker and update ECS service"
                    </div>
        """),
        
        ("What are best practices for using GitHub Copilot CLI?", """
                    <strong>Query formulation:</strong>
                    <ul>
                        <li>✅ Be specific: Include tool names, paths, formats</li>
                        <li>✅ Provide context: Mention OS, environment, constraints</li>
                        <li>✅ State goal clearly: What you want to achieve</li>
                        <li>❌ Avoid vague queries: "fix it", "make it work"</li>
                    </ul>
                    <strong>Safety:</strong>
                    <ul>
                        <li>✅ Always review commands before execution</li>
                        <li>✅ Test in non-production first</li>
                        <li>✅ Use <code>explain</code> for unfamiliar commands</li>
                        <li>✅ Keep backups before destructive operations</li>
                    </ul>
                    <strong>Efficiency:</strong>
                    <ul>
                        <li>✅ Set up shell aliases for frequent use</li>
                        <li>✅ Save useful generated commands for reuse</li>
                        <li>✅ Combine with traditional tools (man, tldr)</li>
                    </ul>
        """),
        
        ("How do you troubleshoot GitHub Copilot CLI issues?", """
                    <strong>Common issues and solutions:</strong>
                    <br><br>
                    <strong>1. Authentication errors:</strong>
                    <div class="code-block">
gh auth status<br>
gh auth refresh
                    </div>
                    <strong>2. Extension not found:</strong>
                    <div class="code-block">
gh extension list<br>
gh extension install github/gh-copilot
                    </div>
                    <strong>3. Outdated version:</strong>
                    <div class="code-block">
gh extension upgrade gh-copilot<br>
gh upgrade  # Update GitHub CLI itself
                    </div>
                    <strong>4. Network issues:</strong>
                    <ul>
                        <li>Check internet connection</li>
                        <li>Verify GitHub API access (firewall/proxy)</li>
                        <li>Test: <code>curl https://api.github.com</code></li>
                    </ul>
                    <strong>5. Subscription issues:</strong>
                    <ul>
                        <li>Verify Copilot license is active</li>
                        <li>Check organization settings</li>
                        <li>Ensure user has seat assigned</li>
                    </ul>
        """),
        
        ("Can GitHub Copilot CLI generate PowerShell commands?", """
                    <strong>Yes!</strong> Full PowerShell support:
                    <br><br>
                    <strong>Example queries:</strong>
                    <div class="code-block">
gh copilot suggest --shell powershell "list all services starting with 'SQL'"<br>
→ Get-Service | Where-Object {$_.Name -like "SQL*"}<br>
<br>
gh copilot suggest --shell powershell "get files modified in last 24 hours"<br>
→ Get-ChildItem -Recurse | Where-Object {$_.LastWriteTime -gt (Get-Date).AddDays(-1)}<br>
<br>
gh copilot suggest --shell powershell "export process list to CSV"<br>
→ Get-Process | Export-Csv -Path processes.csv -NoTypeInformation
                    </div>
                    <strong>PowerShell-specific features:</strong>
                    <ul>
                        <li>Cmdlet suggestions</li>
                        <li>Pipeline operations</li>
                        <li>Object manipulation</li>
                        <li>Windows system administration</li>
                    </ul>
        """),
        
        ("What data does GitHub Copilot CLI send to GitHub?", """
                    <strong>Data transmitted:</strong>
                    <ul>
                        <li><strong>Your query text:</strong> The natural language prompt you provide</li>
                        <li><strong>Shell type:</strong> bash, zsh, PowerShell, etc.</li>
                        <li><strong>OS information:</strong> Operating system type</li>
                        <li><strong>Authentication:</strong> GitHub token for authorization</li>
                    </ul>
                    <strong>NOT transmitted:</strong>
                    <ul>
                        <li>❌ Your command history</li>
                        <li>❌ File contents from your system</li>
                        <li>❌ Directory structure</li>
                        <li>❌ Environment variables</li>
                    </ul>
                    <strong>Data usage:</strong>
                    <ul>
                        <li><strong>Business/Enterprise:</strong> Your queries are NOT used for training</li>
                        <li><strong>Individual:</strong> May be used to improve models</li>
                    </ul>
        """),
        
        ("Can GitHub Copilot CLI replace traditional command-line documentation?", """
                    <strong>No</strong>, it's a complement, not a replacement:
                    <br><br>
                    <strong>GitHub Copilot CLI strengths:</strong>
                    <ul>
                        <li>✅ Quick suggestions for common tasks</li>
                        <li>✅ Natural language interface</li>
                        <li>✅ Cross-tool knowledge</li>
                        <li>✅ Learning aid for new commands</li>
                    </ul>
                    <strong>Traditional docs strengths:</strong>
                    <ul>
                        <li>✅ Comprehensive reference</li>
                        <li>✅ Authoritative information</li>
                        <li>✅ Offline availability</li>
                        <li>✅ Detailed edge cases</li>
                    </ul>
                    <strong>Best approach:</strong> Use Copilot CLI for quick tasks and exploration, then consult official docs for critical operations or deep learning.
        """),
        
        ("How does rate limiting affect GitHub Copilot CLI usage?", """
                    <strong>Rate limits apply:</strong>
                    <ul>
                        <li>Standard GitHub API rate limits</li>
                        <li>Typically 5,000 requests/hour for authenticated users</li>
                        <li>Shared with other GitHub API usage</li>
                    </ul>
                    <strong>Practical impact:</strong>
                    <ul>
                        <li>Normal usage rarely hits limits</li>
                        <li>Issues may occur with automated scripts</li>
                        <li>Heavy users in organizations share limits</li>
                    </ul>
                    <strong>If you hit rate limits:</strong>
                    <div class="code-block">
# Check rate limit status<br>
gh api rate_limit<br>
<br>
# Wait for reset (displayed in response)<br>
# Or use GitHub App for higher limits
                    </div>
        """),
        
        ("Can you create aliases for frequently used Copilot CLI queries?", """
                    <strong>Yes!</strong> Create shell aliases or functions:
                    <br><br>
                    <strong>Bash/Zsh aliases (~/.bashrc or ~/.zshrc):</strong>
                    <div class="code-block">
# Quick suggest<br>
alias ghcs='gh copilot suggest'<br>
alias ghce='gh copilot explain'<br>
<br>
# Domain-specific helpers<br>
alias ghgit='gh copilot suggest --shell bash --domain git'<br>
alias ghdocker='gh copilot suggest --shell bash --domain docker'<br>
<br>
# Custom functions<br>
function ghhelp() {<br>
    gh copilot suggest "how to $*"<br>
}
                    </div>
                    <strong>PowerShell functions (profile.ps1):</strong>
                    <div class="code-block">
function ghcs { gh copilot suggest $args }<br>
function ghce { gh copilot explain $args }
                    </div>
        """)
    ]
    
    content = get_html_template(5, "🖥️ Topic 5: GHC CLI Commands & Limitations", 
                                "25 Comprehensive Questions & Answers", 25,
                                "04-metrics-api.html", "06-usage-analytics.html")
    
    for q, a in qa_list:
        content += qa_item(q, a)
    
    content += get_footer(5)
    
    return content

# Generate all remaining topics
def generate_all_topics():
    topics = [
        (5, generate_topic_05(), "05-cli-commands.html"),
    ]
    
    for topic_num, content, filename in topics:
        filepath = OUTPUT_DIR / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Created: {filename}")

if __name__ == "__main__":
    generate_all_topics()
    print("\n🎉 Topic generation complete!")
