---
keywords: fastai
description: Printing and showing setting up a function 
title: Javascript use in Jupyter Notebook!    
nb_path: _notebooks/2022-09-29-JavaScript.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2022-09-29-JavaScript.ipynb
-->

<div class="container" id="notebook-container">
        
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Writing/Printing-in-JavaScript">Writing/Printing in JavaScript<a class="anchor-link" href="#Writing/Printing-in-JavaScript"> </a></h2>
</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-javascript"><pre><span></span><span class="nx">console</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="s2">&quot;what&#39;s up!&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>what&#39;s up!
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-javascript"><pre><span></span><span class="kd">function</span> <span class="nx">logItType</span><span class="p">(</span><span class="nx">output</span><span class="p">)</span> <span class="p">{</span>
    <span class="nx">console</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="k">typeof</span> <span class="nx">output</span><span class="p">,</span> <span class="s2">&quot;;&quot;</span><span class="p">,</span> <span class="nx">output</span><span class="p">);</span>
<span class="p">}</span>
<span class="nx">console</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="s2">&quot;These are different types outputs in JavaScript&quot;</span><span class="p">)</span>
<span class="nx">logItType</span><span class="p">(</span><span class="s2">&quot;Hi!&quot;</span><span class="p">);</span> <span class="c1">// String</span>
<span class="nx">logItType</span><span class="p">(</span><span class="mf">7</span><span class="p">);</span>    <span class="c1">// Number</span>
<span class="nx">logItType</span><span class="p">([</span><span class="mf">7</span><span class="p">,</span> <span class="mf">8</span><span class="p">,</span> <span class="mf">9</span><span class="p">]);</span>  <span class="c1">// Object is generic for this Array, which similar to Python List</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>These are different types outputs in JavaScript
string ; Hi!
number ; 7
object ; [ 7, 8, 9 ]
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

</div>
 

