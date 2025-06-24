use std::process::Command;
use std::fs::write;

pub fn execute_rust_code(code: &str) -> String {
    let file_path = "temp.rs";
    let output_path = "output";
    match write(file_path, code) {
        Ok(_) => {
            let compile_status = Command::new("rustc")
                .args([file_path, "-o", output_path])
                .status();

            if compile_status.unwrap().success() {
                let output = Command::new(format!("./{}", output_path))
                    .output()
                    .expect("failed to execute compiled code");
                return String::from_utf8_lossy(&output.stdout).to_string();
            } else {
                return "Compilation failed.".to_string();
            }
        }
        Err(e) => format!("Failed to write file: {}", e),
    }
}
