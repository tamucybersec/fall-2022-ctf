; Sections:
section .data
section .bss
section .text
  global _start
; rbp-0x80 = flag
; rbp-0x40 = buf
; rbp-0x84 = iter
; "gigem{this_program_probably_bypasses_most_antivirus}"
; "ghefi~roazU{~bi}q|McfztvzucD~dn~SRGP{HIT\\vKEXDXFBDAN"
; Functions:
_start:
    push    rbp
    mov     rbp, rsp
    sub     rsp, 0x90
    mov     rax, 0x6f727e6966656867
    mov     rdx, 0x7d69627e7b557a61
    mov     QWORD [rbp-0x80], rax
    mov     QWORD [rbp-0x78], rdx
    mov     rax, 0x76747a66634d7c71
    mov     rdx, 0x7e6e647e4463757a
    mov     QWORD [rbp-0x70], rax
    mov     QWORD [rbp-0x68], rdx
    mov     rax, 0x5449487b50475253
    mov     rdx, 0x46584458454b765c
    mov     QWORD [rbp-0x60], rax
    mov     QWORD [rbp-0x58], rdx
    mov     DWORD [rbp-0x50], 0x4e414442
    mov     BYTE [rbp-0x4c], 0x0
    mov rax, 0
    mov rdi, 0
    lea rsi, [rbp-0x40]
    mov rdx, 52
    syscall
    mov DWORD [rbp-0x84], 0
    jmp .loopcheck
.loopstart: mov eax, DWORD [rbp-0x84]
    cdqe
    mov al, BYTE [rbp+rax*1-0x40]
    mov edx, DWORD [rbp-0x84]
    xor edx, eax
    mov eax, DWORD [rbp-0x84]
    cdqe
    mov al, BYTE [rbp+rax*1-0x80]
    cmp dl, al
    jne .bad    
    add DWORD [rbp-0x84], 1
.loopcheck: cmp DWORD [rbp-0x84], 0x33
    jle .loopstart
    mov rax, 0x0a21504559
    mov QWORD [rbp-0x80], rax
    mov rax, 1
    mov rdi, 1
    lea rsi, [rbp-0x80]
    mov rdx, 5
    syscall
    mov rax, 60
    mov rdi, 0
    syscall
.bad mov rax, 0x0a2145504f4e
    mov QWORD [rbp-0x80], rax
    mov rax, 1
    mov rdi, 1
    lea rsi, [rbp-0x80]
    mov rdx, 6
    syscall
    mov rax, 60
    mov rdi, -1
    syscall
