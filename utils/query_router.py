class QueryRouter:

    def classify(self, question):

        question = question.lower()

        if any(word in question for word in [
            "summary",
            "summarize",
            "overview",
            "brief",
            "explain report"
        ]):
            return "summary"

        if any(word in question for word in [
            "compare",
            "difference",
            "versus",
            "vs"
        ]):
            return "compare"

        if any(word in question for word in [
            "page",
            "pages",
            "file",
            "pdf",
            "document"
        ]):
            return "metadata"

        return "rag"