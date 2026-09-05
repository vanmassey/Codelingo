import argparse
import sys
from engine import code_engine

def main():
    # 1. Initialize the command-line argument parser engine
    parser = argparse.ArgumentParser(
        description="Codelingo CLI (cdli) - Multilingual Code Reference Engine"
    )
    
    # 2. Add positional commands to match our target syntax format
    parser.add_argument("action", choices=["get", "status"], help="The CLI action to perform")
    parser.add_argument("prog_lang", nargs="?", help="Target programming language (e.g., python, go)")
    parser.add_argument("human_lang", nargs="?", help="Target instruction human language (e.g., en, es)")

    args = parser.parse_args()

    # 3. Handle status updates
    if args.action == "status":
        print("\n=== Codelingo CLI (cdli) System Matrix ===")
        print("Status: Online")
        print("Engine: Pandas DataFrame Data Core Core")
        print("Supported Programming Languages: python, go")
        print("Supported Human Languages: en (English), es (Spanish)\n")
        sys.exit(0)

    # 4. Handle snippet queries
    if args.action == "get":
        if not args.prog_lang or not args.human_lang:
            print("Error: The 'get' command requires both [programming_lang] and [human_lang].")
            print("Usage example: cdli get python es")
            sys.exit(1)
            
        result = code_engine.query_matrix(args.prog_lang, args.human_lang)
        
        if not result:
            print(f"\nError: Snippet translation matrix not found for '{args.prog_lang}' in '{args.human_lang}'.")
            print("Run 'cdli status' to verify the supported language options.\n")
            sys.exit(1)
            
        # 5. Output the successful result matrix right into the terminal
        print(f"\n--- {result['title']} ({args.prog_lang.upper()}) ---")
        print(result["code_content"])
        print("-" * 40 + "\n")

if __name__ == "__main__":
    main()
