---
keywords: fastai
title: Title
nb_path: _notebooks/2022-09-21-GradeCalculator.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2022-09-21-GradeCalculator.ipynb
-->

<div class="container" id="notebook-container">
        
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-python"><pre><span></span>
</pre></div>

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
<div class=" highlight hl-python"><pre><span></span><span class="n">StudentInfo</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">StudentInfo</span><span class="o">.</span><span class="n">append</span><span class="p">({</span>
    <span class="s2">&quot;Student Name&quot;</span><span class="p">:</span> <span class="s2">&quot;Joselyn Anda&quot;</span><span class="p">,</span>
    <span class="s2">&quot;Grade&quot;</span><span class="p">:</span> <span class="s2">&quot;11, Junior&quot;</span>
    <span class="s2">&quot;Period&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span>
<span class="p">})</span>
</pre></div>

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
<div class=" highlight hl-python"><pre><span></span><span class="k">def</span> <span class="nf">questions_and_answer</span><span class="p">(</span><span class="n">prompt</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;question&quot;</span> <span class="o">+</span> <span class="n">prompt</span><span class="p">)</span>
      <span class="n">msg</span> <span class="o">=</span> <span class="nb">input</span><span class="p">()</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Answer: &quot;</span> <span class="o">+</span> <span class="n">msg</span><span class="p">)</span>
    
<span class="k">def</span> <span class="nf">question_with_response</span><span class="p">(</span><span class="n">prompt</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Question: &quot;</span> <span class="o">+</span> <span class="n">prompt</span><span class="p">)</span>
    <span class="n">msg</span> <span class="o">=</span> <span class="nb">input</span><span class="p">()</span>
    <span class="k">return</span> <span class="n">msg</span>

<span class="n">questions</span> <span class="o">=</span> 
<span class="n">correct</span> <span class="o">=</span> <span class="mi">0</span>  

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Fill in the following information to calculate your grade average.&quot;</span><span class="p">)</span>

<span class="n">rsp</span> <span class="o">=</span> <span class="n">question_with_response</span><span class="p">(</span><span class="s2">&quot;What is your name?&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Hi &quot;</span> <span class="o">+</span> <span class="n">rsp</span> <span class="o">+</span> <span class="s2">&quot; nice to meet you :)&quot;</span><span class="p">)</span>

<span class="n">rsp</span> <span class="o">=</span> <span class="n">question_with_response</span><span class="p">(</span><span class="s2">&quot;Do you have a dog?&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot; Me too! &quot;</span><span class="p">)</span>

<span class="n">rsp</span> <span class="o">=</span> <span class="n">question_with_response</span><span class="p">(</span><span class="s2">&quot;Is/are your dog(s) a boy or a girl?&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot; Oh &quot;</span> <span class="o">+</span> <span class="n">rsp</span> <span class="o">+</span> <span class="s2">&quot;  Cool, I have 2 girls &quot;</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">print_data</span><span class="p">(</span><span class="n">d_rec</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">d_rec_</span><span class="p">[</span><span class="s2">&quot;Student Name&quot;</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

</div>
    {% endraw %}

</div>
 

