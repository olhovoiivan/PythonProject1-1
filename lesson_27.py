from bs4 import BeautifulSoup, Tag
from typing import List, Any

class DOMTreeNode:
    def __init__(self, tag_name: str, text_content: str = None):
        self.tag_name = tag_name.lower()
        self.text_content = text_content
        self.children: List['DOMTreeNode'] = []

    def add_child(self, child_node: 'DOMTreeNode'):
        self.children.append(child_node)
    
    def __repr__(self):
        return f"<{self.tag_name}> (Text: {self.text_content[:20] if self.text_content else 'None'})"

def build_custom_dom(soup_node: Any) -> DOMTreeNode:
    if isinstance(soup_node, Tag):
        tag_name = soup_node.name
        text_content = soup_node.get_text(separator=" ", strip=True) 
        current_node = DOMTreeNode(tag_name, text_content)
        for child in soup_node.contents:
            if isinstance(child, Tag):
                child_node = build_custom_dom(child)
                current_node.add_child(child_node)
        return current_node
    elif hasattr(soup_node, 'contents'):
        for content in soup_node.contents:
            if isinstance(content, Tag):
                return build_custom_dom(content) 
    return None 

def find_text_by_tag(root_node: DOMTreeNode, target_tag: str) -> List[str]:
    target_tag = target_tag.lower()
    results = []
    stack = [root_node]
    while stack:
        current = stack.pop()
        if current is None:
            continue
        if current.tag_name == target_tag:
            if current.text_content:
                results.append(current.text_content)
        stack.extend(reversed(current.children)) 
    return results

# --- ВХІДНІ ДАНІ ТА ВИКОНАННЯ ---

html_input_complex = """
<html>
  <head>
    <title>Приклад DOM</title>
  </head>
  <body>
    <header>
        <h1>Привіт!</h1>
    </header>
    <section id="content">
        <p class="first">Як справи?</p>
        <div>
            <p>Яка погода?</p>
        </div>
        <p>Яка мова?</p>
    </section>
  </body>
</html>
"""
target_tag = "p"
# 1. Побудова DOM-дерева BeautifulSoup
soup = BeautifulSoup(html_input_complex, 'html.parser')
print(" DOM-дерево BeautifulSoup успішно побудовано.")
# 2. Побудова нашої кастомної структури дерева
custom_dom_root = build_custom_dom(soup)
print(" Кастомне DOM-дерево (клас DOMTreeNode) успішно побудовано.")
# 3. Пошук тексту за заданим тегом
found_texts = find_text_by_tag(custom_dom_root, target_tag)
# Вихідні дані: текст
print(f"\n--- Результати Пошуку ---")
print(f"Тег для пошуку: <{target_tag}>")
if found_texts:
    print("\nЗнайдений текст:")
    for i, text in enumerate(found_texts):
        print(f"{i+1}. {text}")
else:
    print(f"\nТекст для тегу <{target_tag}> не знайдено.")
# Приклад пошуку тегу 'h1'
found_h1 = find_text_by_tag(custom_dom_root, 'h1')
print(f"\nЗнайдений текст для тегу <h1>: {found_h1[0] if found_h1 else 'None'}")
