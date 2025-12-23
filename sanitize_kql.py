import re
import argparse
import os

def sanitize_content(content):
    # Regex patterns
    ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    guid_pattern = r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b'
    # Simple email pattern
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # IPv6 pattern (simplified, covers common forms)
    ipv6_pattern = r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b|\b((?:[0-9A-Fa-f]{1,4}(?::[0-9A-Fa-f]{1,4})*)?::(?:[0-9A-Fa-f]{1,4}(?::[0-9A-Fa-f]{1,4})*)?)\b'
    
    # Replacements
    sanitized = re.sub(ipv4_pattern, '<IP_ADDRESS>', content)
    sanitized = re.sub(guid_pattern, '<GUID>', sanitized)
    sanitized = re.sub(email_pattern, '<EMAIL>', sanitized)
    sanitized = re.sub(ipv6_pattern, '<IPV6_ADDRESS>', sanitized)
    
    return sanitized

def process_file(input_path, output_path=None):
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        sanitized_content = sanitize_content(content)
        
        if output_path:
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(sanitized_content)
            print(f"Processed: {input_path} -> {output_path}")
        else:
            print(f"--- Sanitized Output for {input_path} ---")
            print(sanitized_content)
            print("-------------------------------------------")
            
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Sanitize KQL queries of sensitive data.")
    parser.add_argument('--file', help="Path to a single KQL file to sanitize.")
    parser.add_argument('--input', help="Input directory containing KQL files.")
    parser.add_argument('--output', help="Output directory to save sanitized files.")
    
    args = parser.parse_args()
    
    if args.file:
        output_file = None
        if args.output:
            # If output is a dir, append filename, else treat as filepath
            if os.path.isdir(args.output):
                output_file = os.path.join(args.output, os.path.basename(args.file))
            else:
                output_file = args.output
        process_file(args.file, output_file)
        
    elif args.input and args.output:
        if not os.path.isdir(args.input):
            print(f"Error: {args.input} is not a directory.")
            return
            
        for root, _, files in os.walk(args.input):
            for file in files:
                if file.endswith('.kql') or file.endswith('.txt'):
                    input_path = os.path.join(root, file)
                    # Maintain relative structure
                    rel_path = os.path.relpath(input_path, args.input)
                    output_path = os.path.join(args.output, rel_path)
                    process_file(input_path, output_path)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
