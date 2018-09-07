code SEGMENT

    ASSUME cs:code,ds:code,ss:stack_seg

    DA DW 0H

    Q  DW  7210H,7811H,6612H,7313H,7514H,7a15H,7616H,6a17H,7018H,7119H,621eH,741fH,6520H,6721H,6822H,6923H,6b24H,6c25H,6d26H,612cH,792dH,642eH,772fH,6330H,6f31H,6e32H

start:

    jmp initial

 

    newinta PROC FAR

    cli

    push dx

    push bx

    push es

    mov ax,code

    mov ds,ax

    mov dx,DA

    inc dx

    cmp dx,02d8h

    js notsub

    sub dx,02d8h

    notsub:

    mov DA,dx

    pop es

    pop bx

    pop dx

    sti

    iret

    newinta ENDP

 

    newintb PROC FAR

    cli

    push ax    push bx    push cx    push dx    push bp    push es    push ds   

    mov ax,code

    mov ds,ax

    mov ax,DA

    cmp ax,016ch

    jb shield   

    in al,060h

    mov bx,0

    redo:

    cmp bx,34h

    je notin   

        mov cx,[Q+bx]

        cmp al,cl

        jne notget       

            push bx

            push ax

            in al,061h

            mov ah,al

            or al,80h

            out 061h,al

            xchg ah,al

            out 061h,al

            pop ax       

            mov al,ch

            mov dx,40h

            mov es,dx

            mov bp,es:[1ch]

            mov es:[bp],ax

            inc bp

            inc bp

            cmp bp,3eh

            jne notend

                mov bp,1eh

            notend:

            mov es:[1ch],bp

            pop bx

            jmp get

        notget:

        inc bx

        inc bx

        jmp redo

    notin:   

    int 2bh

    jmp getout   

    shield:

    in al,061h

    mov ah,al

    or al,80h

    out 061h,al

    xchg ah,al

    out 061h,al

    get:   

    mov al,20h

    out 20h,al

    getout:

    pop ds    pop es    pop bp    pop dx    pop cx    pop bx    pop ax

    sti

    iret

    newintb ENDP

 

initial:mov ax,code

    mov ds,ax

    mov ax,stack_seg

    mov ss,ax

    mov sp,TOP

    mov ax,DA

    xor ax,ax

    mov DA,ax 

    cli   

    mov al,1ch

    mov ah,25h

    mov dx,OFFSET newinta

    int 21h   

    mov al,9h

    mov ah,35h

    int 21h

    mov dx,bx

    mov ax,es

    mov ds,ax

    mov al,2bh

    mov ah,25h

    int 21h   

    mov ax,SEG newintb

    mov ds,ax

    mov al,9h

    mov ah,25h

    mov dx,OFFSET newintb

    int 21h

    sti 

    mov ax,SEG initial

    mov ds,ax

    mov dx,OFFSET initial

    int 27h

 

code ENDS

END start