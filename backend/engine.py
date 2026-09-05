import pandas as pd
from typing import Optional

# Core master matrix mapping programming and human languages
SEED_DATA = [
    {
        "snippet_id": 1,
        "target_prog_lang": "python",
        "target_human_lang": "en",
        "title": "Read a CSV file",
        "code_content": "import pandas as pd\ndf = pd.read_csv('data.csv')"
    },
    {
        "snippet_id": 2,
        "target_prog_lang": "python",
        "target_human_lang": "es",
        "title": "Leer un archivo CSV",
        "code_content": "import pandas as pd\ndf = pd.read_csv('data.csv')"
    },
    {
        "snippet_id": 3,
        "target_prog_lang": "go",
        "target_human_lang": "en",
        "title": "Read a CSV file",
        "code_content": "file, err := os.Open(\"data.csv\")\nif err != nil {\n\tlog.Fatal(err)\n}"
    },
    {
        "snippet_id": 4,
        "target_prog_lang": "go",
        "target_human_lang": "es",
        "title": "Leer un archivo CSV",
        "code_content": "file, err := os.Open(\"data.csv\")\nif err != nil {\n\tlog.Fatal(err)\n}"
    }
]

class CodelingoEngine:
    def __init__(self):
        # Instantiate our engine directly into a Pandas DataFrame matrix
        self.df = pd.DataFrame(SEED_DATA)

    def query_matrix(self, prog_lang: str, human_lang: str) -> Optional[dict]:
        """Filters the pandas snippet matrix by targeting specific language keys."""
        # Standardize strings to prevent case-sensitivity syntax failures
        mask = (self.df["target_prog_lang"] == prog_lang.lower().strip()) & \
               (self.df["target_human_lang"] == human_lang.lower().strip())
        
        filtered_df = self.df[mask]
        
        if filtered_df.empty:
            return None
            
        # Extract the matched record as a standard Python dictionary
        return filtered_df.iloc[0].to_dict()

# Create a global instance for our application routing
code_engine = CodelingoEngine()
