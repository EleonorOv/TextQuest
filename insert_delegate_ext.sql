insert into r_orgreg_delegate(id, org_id, user_ref_id, cio_id)
VALUES ('f9353f83-2b24-46f3-b542-e40ea4a46e0b', '0c8144f5-7fbb-4a68-873a-2b00178cac94',
        '202212140855046170001-78dc7827ab25c104', '44641064764');

insert into r_orgreg_org(id, short_name, inn, branch_code, branch_ref_id)
VALUES ('0c8144f5-7fbb-4a68-873a-2b00178cac94', 'ГАЛЦОВ ВЛАДИМИР ВИКТОРОВИЧ (ИП ГКФХ)', '100700077756', '3500',
        'b02d005b-7311-4155-aa1d-f808c18b58a0');

insert into r_orgreg_org_extsys(id, org_id, external_system_type_id, external_system_id)
values ('90000000-0000-0000-2222-000000000000', '0c8144f5-7fbb-4a68-873a-2b00178cac94', 'CFT', '44613642216');

INSERT INTO r_brchreg_branch (id, branch_type_ref_id, branch_code)
VALUES ('b02d005b-7311-4155-aa1d-f808c18b58a0', '0c8144f5-7fbb-4a68-873a-2b00178cac12', '3500');


insert into r_rbac_actor_permission(subject_ref_id, subject_ref_type, role_signature, business_operation_signature,
                                    channel_auth_types)
values ('f9353f83-2b24-46f3-b542-e40ea4a46e0b', 'ORG_DELEGATE', 'CM_ESPP_REGISTER_ACT', 'CM_ESPP_REGISTER_UPLOAD',
        '{}'::jsonb),
       ('f9353f83-2b24-46f3-b542-e40ea4a46e0b', 'ORG_DELEGATE', 'CM_ESPP_REGISTER_ACT', 'CM_ESPP_REGISTER_DOWNLOAD',
        '{}'::jsonb),
       ('f9353f83-2b24-46f3-b542-e40ea4a46e0b', 'ORG_DELEGATE', 'CM_ESPP_REGISTER_ACT', 'CM_ESPP_REGISTER_HISTORY',
        '{}'::jsonb);

insert into cm_o_espp_bill(id, cft_id, branch_code, created, type, status, file_id, filename, file_size, file_ready,
                           hash, error)
VALUES ('00000000-eeee-0000-0000-000000000000', '44613642216', '3500', now(), 2, 1,
        '00000000-ffff-0000-0000-000000000000',
        'file_1.txt', 10, true, 'hashhhh', null);
userId: fc6f0f8f-021e-48f2-9cb6-f7a88976eedb

clientId: d81e3ebd-38cb-4e88-b251-8226e6d6dd8c
