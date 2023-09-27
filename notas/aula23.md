# Aula PL - 3/05/2022

- Entidades em xml

> Entidades utilizadas atualmente

```
&gt;
&lt;
&amp;
```

->

```xml

<root>
    &gt;
    &lt;
    &amp;
</root>
```

- Elementos que não tem conteudo podem ser descritos desta forma.

```html

<ref entref="e1"/>
==
<ref entref="e1"></ref>
```

- Analisador léxico

```
Simbolos terminais:
{<,>, id, value, =, <?, ?>, text}
```

Precisamos de diferenciar o id, value e o text.
Logo precisamos de estados.

Precisamos de usar uma stack de estados

```py
t.lexer.push_state('STATE')
```